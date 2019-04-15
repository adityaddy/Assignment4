<script type="text/javascript">
    $(document).ready(function() 
    {		
      //the function is called once the document loads     

      $('#hidden-content').load('default.html #experiment', 
              function(response,status,xhr)
      {
        //loads the default.html #lab section into the
        //#hidden-content
		
        $('#container').load('content.html #experiment', 
              function(response,status,xhr)
        {
          //loads the content.html #lab section into the
	  //#container

          homePage=$("div#experiment-header-heading a").html();
          
	  thisPage=$("article#experiment-article header#experiment-article-heading").html();
        
	  breadcrumb="<font color='white'>"+ "<a href='../../index.html'>Home<a/> \> <a href='../index.html'>" + homePage + "</a> \> <a href='index.html'>" + thisPage + "</a>"+ "</font>";
        
	  $("article#experiment-article div#experiment-article-breadcrumb").html(breadcrumb);
				
	  $("#container .default").each(function() 
	  {
            // Extracts all elements with class = "default"
            // and top down
            
	    sectionId = $(this).attr('id');
            sectionContent = $("#hidden-content #" + 
                  sectionId).html();
            $("#container #" + sectionId).html(sectionContent);
	  });
			
	  $("#container #experiment-article-sections > section").each(function() 
	  {
	    // loads all the content in the respective
	    // sections with the corresponding section headings 

            sectionId = $(this).attr('id');
	    headerId = $("#" + sectionId + "-heading").html();
	    iconId = $("#" + sectionId + "-icon").html();

	    $("#container #experiment-article-navigation ul").
	      append("<li> <a href=\'#\' id=\'"+ sectionId + 
              "-menu\'>" + iconId +"<br />" +
              headerId + "</a></li>");
	  });
	
	  /*			
          $("#experiment-article-sections").after(
            "<div id='experiment-article-sections-view'> </div>");
	  $("#experiment-article-sections-view").html($(
            "#experiment-article-sections section:first").html()); */
    
	  $("#experiment-article-sections section").hide();
	  //hide all the experiment sections

	  $("#experiment-article-sections section:first").show();
	  //show only the first experiment section when
	  //the experiment page loads
	  
	  $("#experiment-article-navigation ul > li a").live('click',
            function()            
          {	
            //enables the navigation

            menuId = $(this).attr('id'); 
            // this points to the current element
	    
	    sectionId = menuId.replace(/-menu/i, "");
	    /*
	    $("#experiment-article-sections-view").html($(
            "#experiment-article-sections #" + 
            sectionId).html());
	    */
            
	    $("#experiment-article-sections section").hide();
	    $("#experiment-article-sections #" + sectionId).show();
        });
      });		
    });
  });

  </script>


// ------------------------------------------------------------------------------------------------------------------------

var index;

function getdata(lang,scr){
	$('#fldiv').load('exp2.php?root=%&category=%&gender=%&form=%&person=%&tense=%&reference=%&lang='+lang+'&scr='+scr);
}

function getOption(temp){
	temp1=temp.split("_");
	lang=temp1[0];
	scr=temp1[1];
	document.getElementById("option").innerHTML="";
	document.getElementById("fldiv").innerHTML="";
	if(scr=="null")
	{
		alert("Select language");
		return;
	}
	getdata(lang,scr);
}

function getAnswer(word)
{
	document.getElementById("get_hide").innerHTML="<button onclick=\"hideAnswer('"+word+"');\">Hide Answer</button> <br><br><p style='font-size:20px' > <b>Answer</b>: "+word+"</p>";
}

function hideAnswer(word)
{
	document.getElementById("get_hide").innerHTML="<button onclick=\"getAnswer('"+word+"');\">Get Answer</button>";
}