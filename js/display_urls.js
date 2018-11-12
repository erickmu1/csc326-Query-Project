//Need to show no results appeared if nothing occurs

var page_num = 1;

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
    var table_header = '<p class="table_format"> No results found</p>';
    var url = '';
    var buttons;
    var i;

    if (arr.length < 1){
        table_header = '<p class="table_format"> No results found</p>';
        document.getElementById("table_header").innerHTML=table_header;

    }

    else {
        table_header = '<p class="table_format"> Results</p>';
        document.getElementById("table_header").innerHTML=table_header;

        i = (page_num-1)*5;

        while (i < arr.length){
            if (i < page_num*5){
                url += '<tr class="data"><td class="data"><a class="links" href=' + arr[i] + ' style="text-decoration: none;">' + (i+1) + '. <u>' + arr[i] + '</u></a></td></tr>';
                i++;
            }
            if (i == page_num*5) break;
        }
    }

    document.getElementById("results").innerHTML = url;

    if (arr.length > 5) {
        if (page_num == 1) 
            buttons = '<button onclick="incrPageNum()">Next page</button>';

        else if (page_num < arr.length/5) 
            buttons = '<button onclick="decrPageNum()">Previous page</button> <button onclick="incrPageNum()">Next page</button>';

        else buttons = '<button onclick="decrPageNum()">Previous page</button>';

        document.getElementById("page_buttons").innerHTML = buttons;
    }

}

function incrPageNum(){
    page_num++;
    console.log(page_num);
    loadDoc();
}

function decrPageNum(){
    if (page_num > 1 ){
        page_num--;
        console.log(page_num);
        loadDoc();
    }
}