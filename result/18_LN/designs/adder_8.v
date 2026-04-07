module adder_8 (
    input  [7:0] a,
    input  [7:0] b,
    output [7:0] sum,
    output       cout
);
    assign {cout, sum} = a + b;
endmodule
