import styles from '../layout/Footer.module.css'

function Footer(){
    return(
        <footer>
            <div className="bosch-rights">
                <p>© 2021 Robert Bosch GmbH, all rights reserved</p>
            </div>
            <div className={styles.obligations}>
                <p>Imprint</p>
                <p>Legal informaton</p>
                <p>Data privacy</p>
                <p>Disclosure documents</p>
            </div>
        </footer>
        
    )
}export default Footer