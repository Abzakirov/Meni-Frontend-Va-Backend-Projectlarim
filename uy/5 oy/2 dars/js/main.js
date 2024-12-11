let div = document.createElement('div')
let div2 = document.createElement('div')
let h1 = document.createElement('h1')
let h2 = document.createElement('h2')
let p = document.createElement('p')
let sp = document.createElement('span')
let he = document.createElement('h1')
let fam = document.createElement('h1')
let yo = document.createElement('h3')
let ra = document.createElement('h1')
h1.textContent ="About me"
sp.textContent ='Ism:'
h2.textContent ='Abdulloh'
he.textContent = 'Familiya:'
fam.textContent = 'Zokirov'
yo.textContent = 'Yosh:'
ra.textContent = '15'
div.append(h1,h2,p,sp,he,fam,yo,ra)

document.body.appendChild(div)
div.style.cssText = '  width: 500px;  height: 400px;margin: 0 auto;  background-color: burlywood;border-radius:10px; '
h1.style.cssText = '  font-size: 32px;  text-align: center; padding-top: 45px; color: blue;'
sp.style.cssText = 'font-size: 32px; color: red; padding-left: 115px;' 
h2.style.cssText = 'font-size: 25px; color:#000; padding-left: 185px; position: relative;top: 55px;'
he.style.cssText ='font-size: 30px; color: red; padding-left: 55px;'
fam.style.cssText = 'font-size: 25px; color:#000; padding-left: 185px; position: relative;top: -50px;'
yo.style.cssText = 'font-size: 30px; color: red; padding-left: 105px;position: relative;top: -50px;'
ra.style.cssText = 'font-size: 25px; color:#000; padding-left: 185px; position: relative;top: -110px;'
