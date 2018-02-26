package main

import (
	"io"
	"log"
	"net/http"
	"strings"
)

func main() {
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		buf := make([]byte, 1<<12)
		for {
			bs, err := r.Body.Read(buf[:])
			if err != nil {
				if err == io.EOF {
					res := strings.ToUpper(string(buf[:bs]))
					w.Write([]byte(res))
					return
				}
				log.Println("error: " + err.Error())
				return
			}
			res := strings.ToUpper(string(buf[:bs]))
			w.Write([]byte(res))
		}
	})

	http.ListenAndServe(":8080", nil)
}
