function initViz() {
    var containerDiv = document.getElementById("vizContainer");
    var url = "https://public.tableau.com/views/EmbedTesting/DefensiveStatsAmongNBATeams?:language=en-US&:retry=yes&:display_count=n&:origin=viz_share_link";
    var options = {
        hideTabs: true
    };

    var viz = new tableau.Viz(containerDiv, url, options);

    // var containerDiv2 = document.getElementById("vizContainer2");

    // var viz2 = new tableau.Viz(containerDiv2, url);

    // var url2 = "https://public.tableau.com/views/EmbedTesting/DefensiveStatsAmongNBATeams";

    // var containerDiv3 = document.getElementById("vizContainer3");

    // var viz3 = new tableau.Viz(containerDiv3, url2);
}
