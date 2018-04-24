$( window ).on( "load", function() {
    console.log("2");
    $("a[href='https://jira.gfi.es/secure/MyJiraHome.jspa']").attr('href', 'https://jira.gfi.es/secure/Dashboard.jspa');
    
    console.log(window.location.href)
    if(window.location.href.includes('TempoSearchBoard')) {
        var css = document.createElement("style");
        css.type = "text/css";
        css.innerHTML = ".aui-page-header {\n    visibility: collapse;\n    padding: 0px !important;\n}\n\n.aui-page-header-main {\n    margin-top: 5px;\n    position: absolute;\n    z-index: 10;\n    visibility: visible;\n}\n\n.aui-nav-breadcrumbs {\n    margin-top: 8px !important;\n    float: right;\n}";
        document.body.appendChild(css);
    }

    var tempoButton = "<div id='BOTON-TEMPO-DIV'><a class='BOTON-TEMPO' href='https://jira.gfi.es/secure/TempoSearchBoard!timesheet.jspa?search_filter=38202&use-ISO8061-week-numbers=false&periodType=BILLING&periodView=PERIOD'>TEMPOOO</a></div>";
    var tempoParentID = "gadget-32701-renderbox";
    appendHTMLToElementByID(tempoButton, tempoParentID, "beforeend");

    var jiraFlujoButton = "<a style='margin-left:10px; padding:3px; border:1px solid black;' href='https://delivery.gfi.fr/confluence/display/ISSPS/JIRA?preview=/32345456/32345459/ISSFA-GFI-Gestion_Issues_en_JIRA.PDF'>Flujo JIRA</a>";
    var jiraFlujoParentID = "status-val";
    appendHTMLToElementByID(jiraFlujoButton, jiraFlujoParentID, "afterend");

    console.log("3");
});

function appendHTMLToElementByClass(html, parentClass, position) {
    var parent = document.getElementsByClassName(parentClass);
    if(parent && parent[0] !== null)
        parent[0].insertAdjacentHTML(position, html);
}

//position can be "beforeend", "afterend", etc. look documentation
function appendHTMLToElementByID(html, parentID, position) {
    var parent = document.getElementById(parentID);
    if(parent)
        parent.insertAdjacentHTML(position, html);
}

$(document).click(function() {
  $("#BOTON-TEMPO-DIV").effect("shake");
});




/*$('iframe').on('load', function(){
    totalLabel.style.color = "blue";
});

$('iframe').ready(function(){
    console.log("4");
});*/