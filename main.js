var serialport = require('serialport');
 
// list serial ports:
serialport.list(function (err, ports) {
  ports.forEach(function(port) {
    console.log(port.comName);
  });
});

// comName:"/dev/ttyACM0"
// locationId:undefined
// manufacturer:"Texas Instruments"
// pnpId:"usb-Texas_Instruments_MSP430-USB_Example_168C806E0B002200-if00"
// productId:"0300"
// serialNumber:"168C806E0B002200"
// vendorId:"2047"
var portName = "/dev/ttyACM0";
var myPort = new serialport(portName, 9600);

var Readline = serialport.parsers.Readline; // make instance of Readline parser
var parser = new Readline(); // make a new parser to read ASCII lines
myPort.pipe(parser); // pipe the serial stream to the parser

myPort.on('open', showPortOpen);
parser.on('data', readSerialData);
myPort.on('close', showPortClose);
myPort.on('error', showError);

function showPortOpen() {
  console.log('port open. Data rate: ' + myPort.baudRate);
}

function readSerialData(data) {
  console.log(data);
}

function showPortClose() {
  console.log('port closed.');
}

function showError(error) {
  console.log('Serial port error: ' + error);
}
