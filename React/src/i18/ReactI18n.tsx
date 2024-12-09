import { useTranslation } from "react-i18next";
import './i18n'


export default function ReactI18n() {
    const { t, i18n } = useTranslation();
    const changeLanguage = (lng: string) => {
        i18n.changeLanguage(lng);
    }
    
    
    
    return (
        <div>
            <h1>{t('welcome')}</h1>
            <p>{t('language')}</p>

            <button onClick={() => changeLanguage('en')}>English</button>
            <button onClick={() => changeLanguage('pt')}>Portuguese</button>
        </div>
    );
}