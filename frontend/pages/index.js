import { useRouter } from 'next/router';

export default function Home() {
  const router = useRouter();

  // Redirect to dashboard if logged in, otherwise to login
  if (typeof window !== 'undefined') {
    const token = localStorage.getItem('access_token');
    if (token) {
      router.push('/dashboard');
    } else {
      router.push('/login');
    }
  }

  return (
    <div>
      <p>Redirecting...</p>
    </div>
  );
}