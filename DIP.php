<?php

class PDFBook {
 
    function read() {
        return "reading a pdf book.";
    }
}

class EBookReader {
 
    private $book;
 
    function __construct(PDFBook $book) {
        $this->book = $book;
    }
 
    function read() {
        return $this->book->read();
    }
 
}


$book = new PDFBook();
$read = new EBookReader($b);
 
$read->read();

?>