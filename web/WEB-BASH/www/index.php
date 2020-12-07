<?php
highlight_file(__FILE__);
if(isset($_POST["cmd"]))
{
	$test = $_POST['cmd'];
	$white_list = str_split('${#}\\(<)\'0'); 
	$char_list = str_split($test);
	foreach($char_list as $c){
	    if(!in_array($c,$white_list)){
	            die("Cyzcc");
	        }
	    }
	exec($test);
}
?>