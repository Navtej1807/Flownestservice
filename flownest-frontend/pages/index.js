import Link from 'next/link';

export default function Home() {
  return (
    <div style={{ padding: '20px' }}>
      <h1>Welcome to Flownest AI</h1>
      <Link href="/sql-tuning">
        <button>Go to SQL Tuning</button>
      </Link>
    </div>
  );
}
