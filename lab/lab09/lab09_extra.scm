;; Extra Scheme Questions ;;

; Q5
(define (square x) (* x x))

(define (pow b n)
  'YOUR-CODE-HERE
  (cond
   ((= n 0) 1)
   ((even? n) (square (pow b (/ n 2))))
   (else (* b (pow b  (- n 1))))
   )
)

; Q6
(define lst
  (cons (cons 1 '())
        (cons 2
              (cons (cons 3 4)
                   (cons 5 '()))))
)

; Q7
(define (composed f g)
  (lambda (x) (f (g x)))
)

; Q8
(define (remove item lst)
  'YOUR-CODE-HERE
  (cond
   ((null? lst) '())
   ((equal? item (car lst)) (remove item (cdr lst)))
   (else (cons (car lst) (remove item (cdr lst)))))
)


;;; Tests
(remove 3 nil)
; expect ()
(remove 3 '(1 3 5))
; expect (1 5)
(remove 5 '(5 3 5 5 1 4 5 4))
; expect (3 1 4 4)

; Q9
(define (max a b) (if (> a b) a b))
(define (min a b) (if (> a b) b a))
(define (gcd a b)
  'YOUR-CODE-HERE
  (cond
   ((zero? a) b)
   ((zero? b) a)
   (else (gcd (min a b) (modulo (max a b) (min a b)))))
)

;;; Tests
(gcd 24 60)
; expect 12
(gcd 1071 462)
; expect 21

; Q10
(define (no-repeats s)
  'YOUR-CODE-HERE
  (if (null? s) '()
      (cons (car s)
            (no-repeats (filter (lambda (x) (not (= x (car s)))) (cdr s)))))
)

; Q11
(define (substitute s old new)
  'YOUR-CODE-HERE
  (cond
   ((null? s) nil)
   ((pair? (car s))
    (cons (substitute (car s) old new) (substitute (cdr s) old new)))
   (else
    (if (equal? (car s) old)
        (cons new (substitute (cdr s) old new))
          (cons (car s) (substitute (cdr s) old new)))))
 )

; Q12
(define (sub-all s olds news)
  'YOUR-CODE-HERE
  (if (null? olds)
      s
      (sub-all(substitute s (car olds) (car news)) (cdr olds) (cdr news)))
)