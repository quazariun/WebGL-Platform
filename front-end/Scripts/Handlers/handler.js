export async function loadFile(nome) {
    let result;

    await fetch('http://127.0.0.1:3000/Models/Geometries/' + nome)
        .then(response => response.json())
        .then(json => result = json);

    return result;
}