$(document).ready(
  $("#update-btn").click(function (event) {
    event.preventDefault();

    $(".update-form").toggle();
  }),

  $("#part-time").click(function (event) {
    event.preventDefault();
    $("#full-time").hide();
    $(".or").hide();
    $("#part-time").hide();

    //get the target div you want to append/prepend to
    var someDiv = document.getElementById("addHere");

   //append text
   someDiv.innerHTML +=
   "<div class='bg-light'> \
   <p>You have selected Part Time mode </p> </div>";

    //prepend text
    someDiv.innerHTML = "<div class='h4'> <strong>Part Time Basis</strong> </div> <hr/>"  + someDiv.innerHTML;
    // $("#addHere").HTML("<p>You have selected Part Time Rates</p>");
  }),


  $("#full-time").click(function (event) {
    event.preventDefault();
    $("#part-time").hide();
    $(".or").hide();
    $("#full-time").hide();

    //get the target div you want to append/prepend to
    var someDiv = document.getElementById("addHere");

    //append text
    someDiv.innerHTML +=
      "<div class='bg-light'> \
      <p>You have selected full Time mode </p> </div>";

    //prepend text
    someDiv.innerHTML = "<div class='h4'> <strong>Full Time Basis</strong> </div> <hr/>"  + someDiv.innerHTML;
  
  })

  // function addText() {
  //   document.getElementById("addHere").innerHTML +=
  //     "<p>You have selected Part Time Rates</p>";
  // }
);
