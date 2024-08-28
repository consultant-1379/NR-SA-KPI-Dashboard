if($("#docPropStatus").text().trim()=="DL MAC DRB Throughput per QoS" ||
$("#docPropStatus").text().trim()=="Average Overall DL Latency per QoS" ||
$("#docPropStatus").text().trim()=="Average DL MAC DRB Latency per QoS covering non-DRX In-sync" ||
$("#docPropStatus").text().trim()=="Average DL MAC DRB Latency per QoS covering DRX In-sync"
){
$("#qos").show()
console.log("First")
}else{
$("#qos").hide()
console.log("Second")
}
