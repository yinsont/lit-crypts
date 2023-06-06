import React, { useEffect, useState } from 'react';
import { BrowserRouter as Router, Route } from 'react-router-dom';

function Example() {
const [data, setData] = useState(null);

useEffect(() => {
fetch('http://127.0.0.1:5000/example')
.then(response => response.json())
.then(data => setData(data));
}, []);

return (
    'Hello World'
)
// return (
// <div>
// {data && <div>{data.message}</div>}
// </div>
// );
// }

}
export default Example;
