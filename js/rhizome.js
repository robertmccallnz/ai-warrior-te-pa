// Interactive rhizome mapper using vis-network (loaded via CDN)
// Reads two sources:
//   - data/rhizome.json      → the permanent, hand-curated structure
//   - data/rhizome-live.json → weekly scan findings (news, panui, parliament) that grow off the permanent nodes
async function initRhizome() {
  const container = document.getElementById('rhizome');
  if (!container) return;

  const [baseRes, liveRes] = await Promise.all([
    fetch('data/rhizome.json'),
    fetch('data/rhizome-live.json').catch(() => null)
  ]);
  const base = await baseRes.json();
  const live = liveRes && liveRes.ok ? await liveRes.json() : { nodes: [], edges: [], updated_at: null };

  // Merge — live nodes/edges are appended. IDs prefixed with 'live-' by the scan.
  const data = {
    nodes: [...base.nodes, ...(live.nodes || [])],
    edges: [...base.edges, ...(live.edges || [])]
  };

  // Show 'last updated' banner
  const stamp = document.getElementById('rhizome-updated');
  if (stamp) {
    if (live.updated_at) {
      const dt = new Date(live.updated_at);
      stamp.textContent = `Live layer · ${(live.nodes || []).length} findings · last scan ${dt.toLocaleDateString('en-NZ', { day:'numeric', month:'short', year:'numeric' })}`;
    } else {
      stamp.textContent = `Live layer · awaiting first Monday scan`;
    }
  }

  const groupStyle = {
    core:     { color: { background: '#a4181a', border: '#0f0b09' }, font: { color: '#f5efe4', size: 20, face: 'Fraunces, serif' }, shape: 'ellipse' },
    leader:   { color: { background: '#0f0b09', border: '#a4181a' }, font: { color: '#f5efe4', size: 14 }, shape: 'ellipse' },
    mp:       { color: { background: '#2b1a12', border: '#c65a2e' }, font: { color: '#f5efe4', size: 13 }, shape: 'ellipse' },
    iwi:      { color: { background: '#3a5a3a', border: '#0f0b09' }, font: { color: '#f5efe4', size: 13 }, shape: 'hexagon' },
    kaupapa:  { color: { background: '#d9a441', border: '#0f0b09' }, font: { color: '#0f0b09', size: 14, face: 'Fraunces, serif' }, shape: 'diamond' },
    policy:   { color: { background: '#1c3f57', border: '#0f0b09' }, font: { color: '#f5efe4', size: 13 }, shape: 'box' },
    campaign: { color: { background: '#c65a2e', border: '#0f0b09' }, font: { color: '#f5efe4', size: 13 }, shape: 'box' },
    course:   { color: { background: '#efe6d3', border: '#a4181a' }, font: { color: '#0f0b09', size: 12 }, shape: 'box' },
    fund:     { color: { background: '#f5efe4', border: '#3a5a3a' }, font: { color: '#0f0b09', size: 12 }, shape: 'dot', size: 22 },
    // Live layer — glowing, dashed borders, distinct shapes
    news:       { color: { background: '#fff3d6', border: '#a4181a' }, font: { color: '#0f0b09', size: 12 }, shape: 'star', borderWidthSelected: 4 },
    panui:      { color: { background: '#a4181a', border: '#d9a441' }, font: { color: '#f5efe4', size: 12 }, shape: 'triangle' },
    parliament: { color: { background: '#1c3f57', border: '#d9a441' }, font: { color: '#f5efe4', size: 12 }, shape: 'triangleDown' }
  };

  const liveGroups = new Set(['news','panui','parliament']);

  const nodes = data.nodes.map(n => {
    const style = groupStyle[n.group] || {};
    const isLive = liveGroups.has(n.group);
    const currentLang = (window.AIW_I18N && window.AIW_I18N.current()) || 'en';
    const label = (currentLang === 'mi' && n.label_mi) ? n.label_mi : n.label;
    const node = {
      id: n.id,
      label,
      ...style,
      size: n.size || style.size || 18,
      _url: n.url,
      _label_en: n.label,
      _label_mi: n.label_mi || n.label,
      title: n.title || (n.source ? n.source.replace(/\[([^\]]+)\]\([^)]+\)/g, '$1') : undefined),
      borderWidth: isLive ? 3 : 2,
      margin: 10
    };
    if (isLive) node.shapeProperties = { borderDashes: [4, 3] };
    return node;
  });

  const liveEdges = new Set((live.edges || []).map(e => `${e.from}->${e.to}`));
  const edges = data.edges.map(e => {
    const isLive = liveEdges.has(`${e.from}->${e.to}`);
    return {
      from: e.from, to: e.to,
      color: { color: isLive ? 'rgba(217,164,65,0.75)' : 'rgba(15,11,9,0.35)', highlight: '#a4181a' },
      width: isLive ? 2 : 1.4,
      dashes: isLive ? [6, 4] : false,
      smooth: { type: 'continuous', roundness: 0.4 }
    };
  });

  const network = new vis.Network(container, { nodes, edges }, {
    autoResize: true,
    layout: { improvedLayout: true },
    physics: {
      enabled: true,
      solver: 'forceAtlas2Based',
      forceAtlas2Based: { gravitationalConstant: -140, centralGravity: 0.005, springLength: 190, springConstant: 0.06, damping: 0.9, avoidOverlap: 0.8 },
      stabilization: { iterations: 800 }
    },
    interaction: { hover: true, tooltipDelay: 100, zoomView: true, dragView: true },
    nodes: { shadow: { enabled: true, color: 'rgba(0,0,0,0.15)', size: 8, x: 2, y: 3 } }
  });

  // Click a node → open its URL
  network.on('click', params => {
    if (params.nodes && params.nodes.length) {
      const id = params.nodes[0];
      const node = data.nodes.find(n => n.id === id);
      if (node && node.url) {
        if (node.url.startsWith('http')) window.open(node.url, '_blank', 'noopener');
        else location.href = node.url;
      }
    }
  });

  // React to language toggle — refresh labels
  document.addEventListener('langchange', ev => {
    const lang = ev.detail && ev.detail.code;
    const updated = nodes.map(n => ({
      id: n.id,
      label: lang === 'mi' ? n._label_mi : n._label_en
    }));
    network.body.data.nodes.update(updated);
  });

  // Filter controls
  const filterBtns = document.querySelectorAll('.rhizome-filter [data-filter]');
  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const f = btn.dataset.filter;
      const visibleNodeIds = new Set(
        f === 'all' ? data.nodes.map(n => n.id)
                    : data.nodes.filter(n => n.group === f || n.group === 'core').map(n => n.id)
      );
      network.setData({
        nodes: nodes.filter(n => visibleNodeIds.has(n.id)),
        edges: edges.filter(e => visibleNodeIds.has(e.from) && visibleNodeIds.has(e.to))
      });
    });
  });
}
document.addEventListener('DOMContentLoaded', initRhizome);
