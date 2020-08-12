// Select the button
var button = d3.select("#submit");

// Select the form
var form = d3.select("#form");

// Create event handlers for clicking the button or pressing the enter key
button.on("click", runEnter);
form.on("submit",runEnter);

// Create the function to run for both events
function runEnter() {

  // Prevent the page from refreshing
  d3.event.preventDefault();

  // input array:
  to_predict_list = []

  // Select the input element and get the raw HTML node
  var input1 = d3.select("#overall-quality");

  // Get the value property of the input element
  var inputValue1 = input1.property("value");
  to_predict_list.push(inputValue1)

  // Select the input element and get the raw HTML node
  var input2 = d3.select("#ground-area");

  // Get the value property of the input element
  var inputValue2 = input2.property("value");
  to_predict_list.push(inputValue2)

  // Select the input element and get the raw HTML node
  var input3 = d3.select("#second-floor-area");

  // Get the value property of the input element
  var inputValue3 = input3.property("value");
  to_predict_list.push(inputValue3)

  // Select the input element and get the raw HTML node
  var input4 = d3.select("#basement-area");

  // Get the value property of the input element
  var inputValue4 = input4.property("value");
  to_predict_list.push(inputValue4)

  var input5 = d3.select("#first-floor-area");

  // Get the value property of the input element
  var inputValue5 = input5.property("value");
  to_predict_list.push(inputValue5)

  var input6 = d3.select("#lot-area");

  // Get the value property of the input element
  var inputValue6 = input6.property("value");
  to_predict_list.push(inputValue6)

  var input7 = d3.select("#year-built");

  // Get the value property of the input element
  var inputValue7 = input7.property("value");
  to_predict_list.push(inputValue7)

  var input8 = d3.select("#garage-cars");

  // Get the value property of the input element
  var inputValue8 = input8.property("value");
  to_predict_list.push(inputValue8)

  // Print the value to the console
  console.log(to_predict_list);
  return to_predict_list;

}