import './App.css';
import AntDesingExemples from './AntDesingExemples'
import Basic from './Exemples/Basic';
import Hooks from './Exemples/Hooks';
import ReactQueryExemples from './ReactQueryExemples';
import { QueryClientProvider, QueryClient } from 'react-query';
import ReactI18n from './i18/ReactI18n';


function App() {
  const queryClient = new QueryClient()

  return (
    <>
      <AntDesingExemples />
      <Basic />
      <Hooks />
      <QueryClientProvider client={queryClient}>
        <ReactQueryExemples />
      </QueryClientProvider>
      <ReactI18n/>
    </>
  )
}

export default App
