console.log('I am in ')

fetch('/quoteget').then(response=>response.json()).then(data=>{
    let ans = ''
    data.forEach(el => {
       ans+= `<tr>
        <th scope="row">${el.id}</th>
        <td>${el.quote}</td>
        <td>${el.author}</td>      
      </tr>`
    });
    document.getElementById('quotedata').innerHTML = ans
}
    
)