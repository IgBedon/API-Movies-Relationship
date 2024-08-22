import './index.css';
import powerbi from '../../layout/img/powerbi.png';
import axios from 'axios';
import { useState, useEffect } from "react";

function Home() {

    const [filmesFavoritos, setFilmesFavoritos] = useState([])

    useEffect(() => {
        axios
            .get('http://127.0.0.1:8000/api/v1/filmes_favoritos/')
            .then((response) => {
                setFilmesFavoritos(response.data, console.log(response.data))
            })
            .catch((error) => console.log(error))

    }, []);

    function teste(url){
        window.open(url)
    }

    return (

        <div className="content-home">
            <div className='title'>
                <h1></h1>
            </div>

            <div>
                <div className='cards'>
                    {filmesFavoritos.map((item, index) => (
                        <div className='card'>
                            <div className='description'>
                                <div className='title-cards'>
                                    <h1>Usuário: {item.usuario.username}</h1>
                                    <h3>Filme Favorito: {item.filme.titulo}</h3>
                                </div>
                                <div className='down'>
                                    <p>Descrição do Filme: {item.filme.descricao}</p>
                                </div>
                            </div>
                        </div>
                    ))}
                </div>
            </div>
        </div>

    )
}

export default Home