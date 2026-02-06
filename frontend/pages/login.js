import dynamic from 'next/dynamic';

// Dynamically import the Login component to avoid SSR issues
const Login = dynamic(() => import('../src/pages/Login'), {
  ssr: false
});

export default function LoginPage() {
  return <Login />;
}