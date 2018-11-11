<!DOCTYPE html>
<html>
    <head>
        <!-- Retrieving CSS files -->
        <link rel="stylesheet" href="../static/style.css">

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

        <!-- Leave empty for now -->
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


        <!-- Display what user inputted -->
        <section class = "user_input">
            <p class = "user_input">
                Could not find what you were looking for lol. 
                <br>  <a class = "links" href = "{{home_url}}">Click here </a> to go back to main page.
            </p>

        </section>


    </body>
</html> 