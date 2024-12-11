let ures = new Map()
ures.set(1234,"ali")
ures.set(2354,"цali")
ures.set(4223,"sali")
ures.set(6345,"dali")
ures.set(true,"kali")
ures.set(false,"tlkali")
ures.set(null,"kuali")
ures.set(7346,"kuali")
ures.set(4576,"kuali")
console.log(ures)

alert = ures.get(1234)
alert = ures.clear(2354)
alert = ures.delete(4223)
alert = ures.has(6345)
alert = ures.values(true)

// key: 1234, value: Sardor
// key: 2354, value: Sardor
// key: 4223, value: Sardor
// key: 6345, value: Sardor
// key: true, value: Sardor
// key: false, value: Sardor
// key: null, value: Sardor
// key: 7346, value: Sardor
// key: 4576, value: Sardor