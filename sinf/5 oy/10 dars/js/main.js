let Mydiv = document.createElement('div')
Mydiv.innerHTML= `
<h1>Lorem ipsum dolor sit amet.</h1>
<p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Itaque explicabo magnam eveniet cum est vero iusto
    possimus, dolorum ab fugiat sint saepe quia reprehenderit voluptatibus expedita officiis dignissimos,
    placeat impedit.
</p>
<ul>
    <li><a href="#">test</a></li>
    <li><a href="#">test</a></li>
    <li><a href="#">test</a></li>
    <li><a href="#">test</a></li>
    <li><a href="#">test</a></li>
</ul>
`;
let func = document.createDocumentFragment()
func.append(Mydiv)
func.createDocumentFragment()
func()

