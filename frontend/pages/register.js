import dynamic from 'next/dynamic';

// Dynamically import the Register component to avoid SSR issues
const Register = dynamic(() => import('../src/pages/Register'), {
  ssr: false
});

export default function RegisterPage() {
  return <Register />;
}