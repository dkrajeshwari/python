$(function () {
    $("#search").keyup(function () {
        searchStr = $("#search").val()
        if (searchStr.trim() != "") {
            showResult(searchStr);
        }
    })
    $("#idViewall").click(function () {
        $.ajax({
            url: "https://fms-mite.herokuapp.com/fms/",
            method: "GET",
            success: function (data) {
                showTable(data)

            }
        })
    })
    
    function showResult(str) {
        $.ajax({
            url: "https://fms-mite.herokuapp.com/fms/search/" + str,
            method: "GET",
            success: function (data) {
                showTable(data)

            }
        })
    }

    function showTable(data) {
        str = "<table class='table'>";
        str += "<tr><th>Name</th><th>qualification</th><th>Dept</th><th>Status</th></tr>";
        for (i = 0; i < data.length; i++) {
            str += "<tr>";
            str += "<td>" + data[i]["name"] + "</td>";
            str += "<td>" + data[i]["qualification"] + "</td>";
            str += "<td>" + data[i]["deptId"] + "</td>";
            str += "<td>" + data[i]["active"] + "</td>";
            str += "</tr>";
        }
        str += "</table>";
        $("#idTable").html(str);



    }



})
