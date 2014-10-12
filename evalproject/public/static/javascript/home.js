$(document).ready(function(){
    $("#search-button").click(function() {
        var query = $("#search-text-box").val();
        if (query != null && query != "")
        {
            Search(query);
        }
    });

});

function Search(query) {
    $.ajax({
        url:"/search/" + query,
        success: function(result) {
                $("#results").html(result);
            }
    });
}
