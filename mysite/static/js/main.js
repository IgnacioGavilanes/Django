document.onreadystatechange = function () {
  if (document.readyState == "interactive") {
      // Initialize your application or run some code.
      // When the user scrolls the page, execute myFunction
      window.onscroll = function() {stickyScroll()};

      // Get the navbar
      var navbar = document.getElementById("sticky-menu");

      // Get the offset position of the navbar
      var sticky = navbar.offsetTop;

      // Add the sticky class to the navbar when you reach its scroll position. 
      //Remove "sticky" when you leave the scroll position
      function stickyScroll() {
        if (window.pageYOffset >= sticky) {
          navbar.classList.add("sticky")
        } else {
          navbar.classList.remove("sticky");
        }
      }
  }
}


