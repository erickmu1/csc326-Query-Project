<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" href="/static/style.css">
        <link rel="stylesheet" href="/static/search-bar.css">
        <link rel="stylesheet" href="/static/table.css">
        <title>Ace Search Systems</title>
    </head>
    <body>
        <header>

        </header>

        <section class = "search_brand">
                <p class = "brand_name"> Ace Search Systems </p>
                <img class = "logo" src = "images/ace-logo.jpg"  Alt="Ace Search Systems Logo"> 
        </section>


        <div class = "search_bar">
       
            <form action="/" method="post">
                <input class = "search_input" name="keywords" type="text" placeholder="Type to search"/>
                <input class = "search_button" value="Go!" type="submit" />
            </form> 

        </div>

        <section class = "user_input">
            %if user_input == None and start_site == False: 
                <p class = "user_input">Sorry, that is not a valid search.</p>

            %elif user_input != None:
                <p class = "user_input">Searched for: "{{user_input}}"</p>

            %end

        </section>

        <div class="table_format">
            <table id="results" class = "results_format">
                <tr class = "table_header">
                    <td><b>Searched Word</b></td>
                    <td><b>Count</b></td>    
                </tr>

                %for keyword in keywords_list:
                    <tr class = "table_results">
                        <td>{{keyword}}</td>
                        <td>{{keywords_list[keyword]}}</td>
                    <tr>
                %end

            </table>


            <table id="history" class = "results_format">

                <tr class = "table_header">
                    <td><b>Top 20 Words</b></td>
                    <td><b>Count</b></td>    
                </tr>

                %for popular in popular_list:
                    <tr class = "table_results">
                        <td>{{popular[0]}}</td>
                        <td>{{popular[1]}}</td>
                    <tr>
                %end


            </table>
        </div>

    </body>
</html> 


