import React from 'react'
import { getSharkList } from "../helper/sharkListHelper.js";

function MyApp({ Component, pageProps }) {

  const [sharks,getSharks] = React.useState([]);

  React.useEffect(() => {
    getSharkList()
    .then(response=>{
      getSharks({sharks:response}),
      console.log(response);
    })
    .catch(error=>console.log(error))
  }, []);

  return(
    <div>Hey there!</div>
  );
}

export default MyApp
