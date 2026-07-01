// Interactive rhizome mapper using vis-network (loaded via CDN)
async function initRhizome() {
  const container = document.getElementById('rhizome');
  if (!container) return;

  const res = await fetch('data/rhizome.json');
  const data = await res.json();

  const groupStyle = {
    core:     { color: { background: '#a4181a', border: '#0f0b09' }, font: { color: '#f5efe4', size: 20, face: 'Fraunces, serif' }, shape: 'ellipse' },
    leader:   { color: { background: '#0f0b09', border: '#a4181a' }, font: { color: '#f5efe4', size: 14 }, shape: 'ellipse' },
    mp:       { color: { background: '#2b1a12', border: '#c65a2e' }, font: { color: '#f5efe4', size: 13 }, shape: 'ellipse' },
    iwi:      { color: { background: '#3a5a3a', border: '#0f0b09' }, font: { color: '#f5efe4', size: 13 }, shape: 'hexagon' },
    kaupapa:  { color: { background: '#d9a441', border: '#0f0b09' }, font: { color: '#0f0b09', size: 14, face: 'Fraunces, serif' }, shape: 'diamond' },
    policy:   { color: { background: '#1c3f57', border: '#0f0b09' }, font: { color: '#f5efe4', size: 13 }, shape: 'box' },
    campaign: { color: { background: '#c65a2e', border: '#0f0b09' }, font: { color: '#f5efe4', size: 13 }, shape: 'box' },
    course:   { color: { background: '#efe6d3', border: '#a4181a' }, font: { color: '#0f0b09', size: 12 }, shape: 'box' },
    fund:     { color: { background: '#f5efe4', border: '#3a5a3a' }, font: { color: '#0f0b09', size: 12 }, shape: 'dot', size: 22 }
  };

  const nodes = data.nodes.map(n => ({
    id: n.id,
    label: n.label,
    ...(groupStyle[n.group] || {}),
    size: n.size || (groupStyle[n.group]?.size) || 18,
    _url: n.url,
    borderWidth: 2,
    margin: 10
  }));

  const edges = data.edges.map(e => ({
    from: e.from, to: e.to,
    color: { color: 'rgba(15,11,9,0.35)', highlight: '#a4181a' },
    width: 1.4,
    smooth: { type: 'continuous', roundness: 0.4 }
  }));

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
