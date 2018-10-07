<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
	    <link rel="stylesheet" href="/style.css">
        <title>Page Title</title>
    </head>
    <body>


        <table id=”results”>
            <h1></h1>
            %if user_input != None:
                <p>Search for "{{user_input}}"</p>
            %end

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

        <form action="/" method="post">
            <input name="keywords" type="text" />
            <input value="Count" type="submit" />
        </form> 

        <table id="history">

            <tr>
                <td><b>Top 20 Words</b></td>
                <td><b>Count</b></td>    
            </tr>

            %for popular in popular_list:
                <tr>
                    <td>{{popular[0]}}</td>
                    <td>{{popular[1]}}</td>
                <tr>
            %end


        </table>

    </body>
</html> 


