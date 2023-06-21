async function getQuote(){
    const response = await axios.get('https://api.goprogram.ai/inspiration')
        

        // create elements
        let h1 = document.createElement("h1")
        let h5 = document.createElement("h5")
    
        // modify elements
        h1.textContent = `Author: ${response.data.author}`
        h5.textContent = `QOTD: ${response.data.quote}`
    
        // add elements to DOM
        document.body.appendChild(h5)
        document.body.appendChild(h1)
            
 }

getQuote()
