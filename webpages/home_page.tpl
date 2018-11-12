<!DOCTYPE html>
<html>
    <head>
        <!-- Retrieving CSS files -->
        <link rel="stylesheet" href="../style/general.css">
        <link rel="stylesheet" href="../style/brand.css">
        <link rel="stylesheet" href="../style/search-bar.css">
        <link rel="stylesheet" href="../style/table.css">
        <link rel="stylesheet" href="../style/buttons.css">

        <script type="text/javascript" src="../js/display_urls.js"></script>
        <script type="text/javascript" src="../js/require.js"></script>

        <title>Ace Search Systems</title>

        <style>
        .right {
            float: right;
            width: 100px;
            padding: 10px;
        }
        .left {
            float: left;
            width: 100px;
            padding: 10px;
        }
        p.email{
            font-family: Rockwell, sans-serif;
            color: white;
            font-size: 1.0em;
            text-align: left;

            padding:0;
            margin:0;
        }
        </style>
    </head>
    <body>
        <header>
            <!-- Sign In Button -->
            <div class="right">
                <form action="/" method="post">
                    %if user is None:
                        <input type="submit" name="SignIn" value="Sign In"/>
                    %else:
                        <input type="submit" name="SignOut" value="Sign Out"/>
                    %end
                </form>
            </div>

            <!-- User Identifier -->
            <div class="left">
            %if user is not None:
                <p class = "email">Welcome!<br>{{user['email']}}</p>
            %end
            </div>


        </header>
        <!-- Brand name and logo -->
        <section class = "search_brand">
                <p class = "brand_name"> Ace Search Systems </p>
                <img class = "logo" src = "../images/ace-logo.jpg"  Alt="Ace Search Systems Logo"> 
        </section>

        <!-- Search bar -->
        <div class = "search_bar">
       
            <form action="/" method="post">
                <input class = "search_input" name="keywords" type="text" placeholder="Type to search"/>
                <input onclick="loadDoc()" class = "search_button" value="Go!" type="submit" />
            </form> 

        </div>

        <!-- Display what user inputted -->
        <section class = "user_input">
            %if user_input == None and start_site == False: 
                <p class = "user_input">Sorry, that is not a valid search.</p>

            %elif user_input != None:
                <p class = "user_input">Searched for: "{{user_input}}"</p>

            %end

        </section>

        <!-- Table of results and result history -->
        <!-- %if user is not None: -->
        <div class="table_format">
            <table id="results" class="results_format">
        </div>
        <!-- %end -->
        
        <div id="page_buttons">

        </div>


        <script type = "text/javascript">
            loadDoc();
        </script>

    </body>


</html> 


