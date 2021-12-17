$(function(){
	(function() {
	  let onpageLoad = localStorage.getItem("theme") || "";
	  let element = document.body;
	  element.classList.add(onpageLoad);
	  document.getElementById("theme").textContent =
	    localStorage.getItem("theme") || "light";
	})();

	function themeToggle() {
	  let element = document.body;
	  element.classList.toggle("dark-mode");

	  let theme = localStorage.getItem("theme");
	  if (theme && theme === "dark-mode") {
	    localStorage.setItem("theme", "");
	  } else {
	    localStorage.setItem("theme", "dark-mode");
	  }

	  document.getElementById("theme").textContent = localStorage.getItem("theme");
	}

	function myFunction() {
	  var input, filter, ul, li, a, i, txtValue;
	  input = document.getElementById("myInput");
	  filter = input.value.toUpperCase();
	  ul = document.getElementById("hello");
	  li = ul.getElementsByTagName("p");
	  for (i = 0; i < li.length; i++) {
	      a = li[i].getElementsByTagName("a")[0];
	      txtValue = a.textContent || a.innerText;
	      if (txtValue.toUpperCase().indexOf(filter) > -1) {
	          li[i].style.display = "";
	      } else {
	          li[i].style.display = "none";
	      }
	  }
	}

	function darkmode(){
	  var element = document.body;
	     element.classList.toggle("dark-mode");
	     if ($("#darkmodebtn").val()==0){
	       $("#darkmodebtn").val(1);
	     }
	     else{
	       $("#darkmodebtn").val(1);
	     }
	}

});
