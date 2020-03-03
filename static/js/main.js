$(document).ready(function() {
    $('.collapsible').collapsible();
    $('select').material_select();
    $('.button-collapse').sideNav();
    $('.parallax').parallax();
});
/* Using datepicker from course mini project */
$('.datepicker').pickadate({
    selectMonths: true,
    selectYears: 15,
    today: 'Today',
    clear: 'Clear',
    close: 'Ok',
    closeOnSelect: false
});

function datePickerSetUp()  {
    var datePickerContainer = document.getElementById("matfix");
    if (datePickerContainer != null){
        datePickerContainer.addEventListener("click", function (e) {
            e.stopPropagation();
        });
    }    
}
/* I use Materialize for card reveal, but wanted to change it to reveal the summary by hover.
I got the solution from stack overflow: https://bit.ly/39S4X6f */ 
$(function () {
    $('.card').hover(
        function () {
            $(this).find('> .card-image > img.activator').click();
        }, function () {
            $(this).find('> .card-reveal > .card-title').click();
        }
    );
});

datePickerSetUp();
