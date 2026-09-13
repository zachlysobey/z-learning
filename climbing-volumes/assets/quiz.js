// Minimal retrieval-practice quiz. Usage in a lesson:
//
//   <div class="quiz" data-quiz></div>
//   <script src="../assets/quiz.js"></script>
//   <script>
//     Quiz(document.querySelector('[data-quiz]'), [
//       { q: 'Delete the word under the cursor?', opts: ['wd', 'dw', 'xd', 'ed'], a: 0,
//         why: 'Select first (w), then act (d).' },
//     ]);
//   </script>
//
// Options are shuffled per load so position gives no clue. Keep every option the
// same length where possible so formatting gives no clue either.

function Quiz(root, questions) {
  let score = 0, answered = 0;
  const scoreEl = document.createElement('div');
  scoreEl.className = 'score';

  questions.forEach((item, i) => {
    const q = document.createElement('div');
    q.className = 'q';
    const p = document.createElement('p');
    p.textContent = (i + 1) + '. ' + item.q;
    q.appendChild(p);

    const order = item.opts.map((_, k) => k).sort(() => Math.random() - 0.5);
    order.forEach(k => {
      const b = document.createElement('button');
      b.className = 'opt';
      b.textContent = item.opts[k];
      b.addEventListener('click', () => {
        if (q.classList.contains('answered')) return;
        q.classList.add('answered');
        answered++;
        if (k === item.a) { b.classList.add('right'); score++; }
        else {
          b.classList.add('wrong');
          [...q.querySelectorAll('.opt')].forEach(o => {
            if (o.textContent === item.opts[item.a]) o.classList.add('right');
          });
        }
        scoreEl.textContent = 'Score: ' + score + ' / ' + answered +
          (answered === questions.length ? ' — done.' : '');
      });
      q.appendChild(b);
    });

    if (item.why) {
      const why = document.createElement('div');
      why.className = 'why';
      why.textContent = item.why;
      q.appendChild(why);
    }
    root.appendChild(q);
  });
  root.appendChild(scoreEl);
}
