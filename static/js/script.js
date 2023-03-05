```javascript code for the back-to-top button functionality:```
$(document).ready(function() {
	// Back to Top Button
	$(".back-to-top").click(function() {
		$("html, body").animate({ scrollTop: 0 }, "slow");
		return false;
	});
});