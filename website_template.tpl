<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" href="/static/style.css">
        <title>Page Title</title>
    </head>
    <body>
        <div class="table_format">
            <table id=”results”>
                <tr>
                    <td><b>Word</b></td>
                    <td><b>Count</b></td>    
                </tr>

                %for keyword in keywords_list:
                    <tr>
                        <td>{{keyword}}</td>
                        <td>{{keywords_list[keyword]}}</td>
                    <tr>
                %end

            </table>
            <div id = "search_bar">
       
                <form action="/" method="post">
                    <input name="keywords" type="text" />
                    <input value="Count" type="submit" />
                </form> 
                
                %if user_input != None:
                <p>Search for "{{user_input}}"</p>
                %end

            </div>
            <table id="history">

                <tr>
                    <td><b>Top 20</b></td>
                    <td><b>Count</b></td>    
                </tr>

                %for popular in popular_list:
                    <tr>
                        <td>{{popular[0]}}</td>
                        <td>{{popular[1]}}</td>
                    <tr>
                %end


            </table>
        </div>

    </body>
</html> 


