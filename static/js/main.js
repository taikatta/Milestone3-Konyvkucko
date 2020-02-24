$(document).ready(function() {
    $('.collapsible').collapsible();
    $('select').material_select();
    $('.button-collapse').sideNav();
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