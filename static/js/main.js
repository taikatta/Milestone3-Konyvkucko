$(document).ready(function() {
    $('.collapsible').collapsible();
    $('select').material_select();
    $('.button-collapse').sideNav();
    $('.parallax').parallax();
});
$('.datepicker').pickadate({
    selectMonths: true, // Creates a dropdown to control month
    selectYears: 15, // Creates a dropdown of 15 years to control year,
    today: 'Today',
    clear: 'Clear',
    close: 'Ok',
    closeOnSelect: false // Close upon selecting a date,
});
document.getElementById("matfix").addEventListener("click", function (e) {
    e.stopPropagation();
});

<!-- I am using Materialize for card reveal, but wanted to change it to reveal the summary by hover. I got the solution from stack overflow: https://bit.ly/39S4X6f -->
$(function () {
    $('.card').hover(
        function () {
            $(this).find('> .card-image > img.activator').click();
        }, function () {
            $(this).find('> .card-reveal > .card-title').click();
        }
    );
});