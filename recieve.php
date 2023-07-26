<?php
  require "config.php";

 //Establish the connection
    $conn = mysqli_init();
    mysqli_ssl_set($conn,NULL,NULL,$sslcert,NULL,NULL);
    if(!mysqli_real_connect($conn, $host, $username, $password, $db_name, 3306, MYSQLI_CLIENT_SSL)){
        die('Failed to connect to MySQL: '.mysqli_connect_error());
    }

    //Test if table exists
    $res = mysqli_query($conn, "SHOW TABLES LIKE 'Products'");

    if (mysqli_num_rows($res) <= 0) {
        echo "<h2>Catalog is empty</h2>";
    } else {
        //Query and print data
        $res = mysqli_query($conn, 'SELECT * FROM Products');

        if (mysqli_num_rows($res) <= 0) {
            echo "<h2>Catalog is empty.</h2>";
        }
        else {
            $arr = array();
            while ($row = mysqli_fetch_assoc($res)) {
                $arr[] = $row;
            }
            echo json_encode($arr);

          
        }
    }

    //Close the connection
    mysqli_close($conn);

    ?>


