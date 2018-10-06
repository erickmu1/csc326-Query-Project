<table id=”results”>

    <tr>
        <td><b>Word</b></td>
        <td><b>Count</b></td>    
    </tr>

    % for keyword in keywords_list:
        <tr>
            <td>{{keyword}}</td>
            <td>{{keywords_list[keyword]}}</td>
        <tr>
    %end

</table>