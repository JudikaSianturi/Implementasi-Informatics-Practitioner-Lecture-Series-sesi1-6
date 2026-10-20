// Data contoh. Ubah nama dan nilai sesuai kebutuhan tugas.
const students = [
  { name: "Andi", score: 85 },
  { name: "Budi", score: 78 },
  { name: "Citra", score: 92 },
  { name: "Deni", score: 80 },
  { name: "Eka", score: 88 }
];

const filter = document.getElementById("studentFilter");
const tableBody = document.getElementById("studentTable");
const rowCount = document.getElementById("rowCount");

// Mengisi pilihan filter dari data yang tersedia.
students.forEach((student) => {
  const option = document.createElement("option");
  option.value = student.name;
  option.textContent = student.name;
  filter.appendChild(option);
});

// Menghitung ringkasan statistik.
const average = students.reduce((sum, student) => sum + student.score, 0) / students.length;
const highest = students.reduce((best, student) =>
  student.score > best.score ? student : best
);

document.getElementById("totalStudents").textContent = students.length;
document.getElementById("averageScore").textContent = average.toFixed(1);
document.getElementById("highestScore").textContent = highest.score;
document.getElementById("highestStudent").textContent = highest.name;

// Membuat grafik batang dengan Chart.js.
const chartContext = document.getElementById("scoreChart");
const scoreChart = new Chart(chartContext, {
  type: "bar",
  data: {
    labels: students.map((student) => student.name),
    datasets: [{
      label: "Nilai",
      data: students.map((student) => student.score),
      backgroundColor: ["#8aa5ff", "#8aa5ff", "#315ee7", "#8aa5ff", "#8aa5ff"],
      borderRadius: 7,
      maxBarThickness: 54
    }]
  },
  options: {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: { display: false },
      tooltip: { callbacks: { label: (context) => `Nilai: ${context.raw}` } }
    },
    scales: {
      y: {
        beginAtZero: true,
        max: 100,
        ticks: { stepSize: 20 },
        grid: { color: "#edf0f5" },
        title: { display: true, text: "Nilai" }
      },
      x: { grid: { display: false } }
    }
  }
});

// Menampilkan data pada tabel dan memperbarui grafik ketika filter berubah.
function renderDashboard(selectedName = "all") {
  const visibleStudents = selectedName === "all"
    ? students
    : students.filter((student) => student.name === selectedName);

  tableBody.innerHTML = "";

  visibleStudents.forEach((student, index) => {
    const row = document.createElement("tr");
    const status = student.score >= 80 ? "Lulus" : "Perlu peningkatan";
    const statusClass = student.score >= 80 ? "status" : "status needs-work";

    row.innerHTML = `
      <td>${index + 1}</td>
      <td>${student.name}</td>
      <td class="score">${student.score}</td>
      <td><span class="${statusClass}">${status}</span></td>
    `;
    tableBody.appendChild(row);
  });

  rowCount.textContent = `${visibleStudents.length} data`;
  scoreChart.data.labels = visibleStudents.map((student) => student.name);
  scoreChart.data.datasets[0].data = visibleStudents.map((student) => student.score);
  scoreChart.data.datasets[0].backgroundColor = visibleStudents.map((student) =>
    student.score === highest.score ? "#315ee7" : "#8aa5ff"
  );
  scoreChart.update();
}

filter.addEventListener("change", (event) => renderDashboard(event.target.value));
renderDashboard();
