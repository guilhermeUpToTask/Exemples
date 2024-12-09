import i18n from 'i18next';
import { initReactI18next } from 'react-i18next';
import HttpBackend from 'i18next-http-backend';
import LanguageDetector from 'i18next-browser-languagedetector';
import translationEN from './locales/en/translation.json'
import translationPT from './locales/pt/translation.json'


const resources = {
    en: {
      translation: translationEN
    },
    pt: {
        translation: translationPT
    }
  }


i18n
  .use(HttpBackend) // Load translations from JSON files
  .use(LanguageDetector) // Detect browser language
  .use(initReactI18next) // Bind react-i18next to i18next
  .init({
    fallbackLng: 'en', // Fallback language
    debug: true,
    interpolation: {
      escapeValue: false, // React already escapes by default
    },
    resources
  });

export default i18n;