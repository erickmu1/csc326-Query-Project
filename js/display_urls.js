//Have a button that "switches to the next page"
//Need to show no results appeared if nothing occurs
//Remove button when user does not type anything
//Rank URLs by their PageRank
//Need to check if file exists

var first_page = true;
var page_num;

function loadDoc(){

    var url = '/json/url_results.json';
    var xhttp = new XMLHttpRequest();

    //Does something when readyState changes
    xhttp.onreadystatechange = function (){

        //readyState = 4 means request is finished and response is ready
        //status = 200 means "OK"
        if (this.readyState == 4 && this.status == 200){
            var myArr = JSON.parse(this.responseText);
            displayURL(myArr); 
        }
    };

    xhttp.open('GET', url, true);
    xhttp.send();
}

function displayURL(arr) {
    var url = '<tr class="table_header"> <td><b>Results</b></td></tr>';
    var buttons;
    var i;

    if (arr.length > 5) {
        if (first_page == true){
            page_num = 1;
            buttons = '<button onclick="incrPageNum()">Next page</button>';
        }

        else if (first_page == false && page_num < arr.length/5) {
            buttons = '<button onclick="decrPageNum()">Previous page</button> <button onclick="incrPageNum()">Next page</button>';
        }


        else {
            buttons = '<button onclick="decrPageNum()">Previous page</button>';
        }


    }


    i = (page_num-1)*5;

    while (i < arr.length){
        if (i < page_num*5){
            url += '<tr class="data"><td class="data"><a class="links" href=' + arr[i] + '>' + arr[i] + '</a></td></tr>';
            i++;
        }
        if (i == page_num*5) break;
    }

    document.getElementById("results").innerHTML = url;

    document.getElementById("page_buttons").innerHTML = buttons;

}

function incrPageNum(){
    page_num++;
    console.log(page_num);
    if (page_num > 1){
        first_page = false;
    }

    loadDoc();


}

function decrPageNum(){
    if (page_num > 1 ){
        page_num--;
        console.log(page_num);
        if (page_num == 1){
            first_page = true;
        }

        loadDoc();
    }


}