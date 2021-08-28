export const getSharkList = () => {
  return fetch(`http://127.0.0.1:8000/api/sharks/`, { method: `GET` })
    .then((response) => {
      return response.json();
    })
    .catch((err) => console.log(err));
};