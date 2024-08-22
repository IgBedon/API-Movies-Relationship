import React from 'react';
import { Link } from 'react-router-dom';
import logo from '../layout/img/bosch-logo.png';
import user from '../layout/img/user.jpg';
import sharebi from '../layout/img/sharebi-logo.png';
import styles from '../layout/Navbar.module.css'; // Importação do arquivo de estilos


function Navbar() {
    return (
        <nav className={styles.nav}>
            <div className={styles.nav}> {/* Aplicação da classe de contêiner */}
                <Link to="/">
                    <img src={logo} alt="bosch" className={styles.logo} /> {/* Aplicação da classe de logo */}
                </Link>
                <div className={styles.user}>
                    <div className=''>
                        <p className='nome'> Davi Lima</p>
                    <p className={styles.area}>GS/OSD</p>
                    </div>
                    <img src={user} alt='user'></img>
                </div>
                <div className={styles.sharebi}>
                    <img src={sharebi} alt='user'></img>
                </div>
            </div>
        </nav>
    );
}

export default Navbar;
