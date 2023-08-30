import './App.css';
import AntDesingExemples from './AntDesingExemples'
import Basic from './Exemples/Basic';
import Hooks from './Exemples/Hooks';
import ReactQueryExemples from './ReactQueryExemples';
import { QueryClientProvider, QueryClient } from 'react-query';


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
    </>
  )
}

export default App
