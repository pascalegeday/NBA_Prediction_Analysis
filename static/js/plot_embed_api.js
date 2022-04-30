import {
    TableauViz,
    TableauEventType,
} from 'https://public.tableau.com/javascripts/api/tableau.embedding.3.latest.min.js';

const viz = new TableauViz();

viz.src = 'https://public.tableau.com/views/EmbedTesting/DefensiveStatsAmongNBATeams?:language=en-US&:retry=yes&:display_count=n&:origin=viz_share_link';
// viz.toolbar = 'hidden';
// viz.height = '400px';
// viz.width = '600px';


document.getElementById('tableauViz').appendChild(viz);
